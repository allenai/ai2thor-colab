from IPython.display import HTML, display
import sys

from moviepy.editor import ImageSequenceClip
from typing import Sequence
import numpy as np
import os
from typing import Optional
import ai2thor.server
from typing import Union
from PIL import Image

import matplotlib.pyplot as plt

__version__ = "<REPLACE_WITH_VERSION>"
__all__ = ["plot_frames", "show_video", "start_xserver", "overlay", "side_by_side"]


def show_objects_table(objects: list) -> None:
    """Visualizes objects in a way that they are clickable and filterable.

    Example:
    event = controller.step("MoveAhead")
    objects = event.metadata["objects"]
    show_objects_table(objects)
    """
    import pandas as pd
    from collections import OrderedDict
    from google.colab.data_table import DataTable

    processed_objects = []
    for obj in objects:
        obj = obj.copy()
        obj["position[x]"] = round(obj["position"]["x"], 4)
        obj["position[y]"] = round(obj["position"]["y"], 4)
        obj["position[z]"] = round(obj["position"]["z"], 4)

        obj["rotation[x]"] = round(obj["rotation"]["x"], 4)
        obj["rotation[y]"] = round(obj["rotation"]["y"], 4)
        obj["rotation[z]"] = round(obj["rotation"]["z"], 4)

        del obj["position"]
        del obj["rotation"]

        # these are too long to display
        del obj["objectOrientedBoundingBox"]
        del obj["axisAlignedBoundingBox"]
        del obj["receptacleObjectIds"]

        obj["mass"] = round(obj["mass"], 4)
        obj["distance"] = round(obj["distance"], 4)

        obj = OrderedDict(obj)
        obj.move_to_end("distance", last=False)
        obj.move_to_end("rotation[z]", last=False)
        obj.move_to_end("rotation[y]", last=False)
        obj.move_to_end("rotation[x]", last=False)

        obj.move_to_end("position[z]", last=False)
        obj.move_to_end("position[y]", last=False)
        obj.move_to_end("position[x]", last=False)

        obj.move_to_end("name", last=False)
        obj.move_to_end("objectId", last=False)
        obj.move_to_end("objectType", last=False)

        processed_objects.append(obj)

    df = pd.DataFrame(processed_objects)
    print(
        "Object Metadata. Not showing objectOrientedBoundingBox, axisAlignedBoundingBox, and receptacleObjectIds for clarity."
    )

    return DataTable(df, max_columns=150, num_rows_per_page=150)


def overlay(
    frame1: np.ndarray,
    frame2: np.ndarray,
    title: Optional[str] = None,
    frame2_alpha: float = 0.75,
) -> None:
    """Blend image frame1 and frame2 on top of each other.

    Example:
    event1 = controller.last_event
    event2 = controller.step("RotateRight")
    overlay(event1.frame, event2.frame)
    """
    fig, ax = plt.subplots(nrows=1, ncols=1, dpi=150, figsize=(4, 5))
    if not (0 < frame2_alpha < 1):
        raise ValueError("frame2_alpha must be in (0:1) not " + frame2_alpha)

    if frame1.dtype == np.uint8:
        frame1 = frame1 / 255
    if frame2.dtype == np.uint8:
        frame2 = frame2 / 255

    ax.imshow(frame2_alpha * frame2 + (1 - frame2_alpha) * frame1)
    ax.axis("off")
    if title:
        fig.suptitle(title, y=0.87, x=0.5125)


def side_by_side(
    frame1: np.ndarray, frame2: np.ndarray, title: Optional[str] = None
) -> None:
    """Plot 2 image frames next to each other.

    Example:
    event1 = controller.last_event
    event2 = controller.step("RotateRight")
    overlay(event1.frame, event2.frame)
    """
    fig, axs = plt.subplots(nrows=1, ncols=2, dpi=150, figsize=(8, 5))
    axs[0].imshow(frame1)
    axs[0].axis("off")
    axs[1].imshow(frame2)
    axs[1].axis("off")
    if title:
        fig.suptitle(title, y=0.85, x=0.5125)


def plot_frames(event: Union[ai2thor.server.Event, np.ndarray]) -> None:
    """Visualize all the frames on an AI2-THOR Event.

    Example:
    plot_frames(controller.last_event)
    """
    if isinstance(event, ai2thor.server.Event):
        frames = dict()
        third_person_frames = event.third_party_camera_frames
        if event.frame is not None:
            frames["RGB"] = event.frame
        if event.instance_segmentation_frame is not None:
            frames["Instance Segmentation"] = event.instance_segmentation_frame
        if event.semantic_segmentation_frame is not None:
            frames["Semantic Segmentation"] = event.semantic_segmentation_frame
        if event.normals_frame is not None:
            frames["Normals"] = event.normals_frame
        if event.depth_frame is not None:
            frames["Depth"] = event.depth_frame

        if len(frames) == 0:
            raise Exception("No agent frames rendered on this event!")

        rows = 2 if len(third_person_frames) else 1
        cols = max(len(frames), len(third_person_frames))
        fig, axs = plt.subplots(
            nrows=rows, ncols=cols, dpi=150, figsize=(3 * cols, 3 * rows)
        )

        agent_row = axs[0] if rows > 1 else axs

        for i, (name, frame) in enumerate(frames.items()):
            ax = agent_row[i] if cols > 1 else agent_row
            im = ax.imshow(frame)
            ax.axis("off")
            ax.set_title(name)

            if name == "Depth":
                fig.colorbar(im, fraction=0.046, pad=0.04, ax=ax)

        # set unused axes off
        for i in range(len(frames), cols):
            agent_row[i].axis("off")

        # add third party camera frames
        if rows > 1:
            for i, frame in enumerate(third_person_frames):
                ax = axs[1][i] if cols > 1 else axs[1]
                ax.imshow(frame)
                ax.axis("off")
            for i in range(len(third_person_frames), cols):
                axs[1][i].axis("off")

            fig.text(x=0.1, y=0.715, s="Agent Frames", rotation="vertical", va="center")
            fig.text(
                x=0.1,
                y=0.3025,
                s="Third Person Frames",
                rotation="vertical",
                va="center",
            )
    elif isinstance(event, np.ndarray):
        return Image.fromarray(event)
    else:
        raise Exception(
            f"Unknown type: {type(event)}. "
            "Must be np.ndarray or ai2thor.server.Event."
        )


def show_video(frames: Sequence[np.ndarray], fps: int = 10):
    """Show a video composed of a sequence of frames.

    Example:
    frames = [
        controller.step("RotateRight", degrees=5).frame
        for _ in range(72)
    ]
    show_video(frames, fps=5)
    """
    frames = ImageSequenceClip(frames, fps=fps)
    return frames.ipython_display()


def start_xserver() -> None:
    """Provide the ability to render AI2-THOR using Google Colab. """
    # Thanks to the [Unity ML Agents team](https://github.com/Unity-Technologies/ml-agents)
    # for most of this setup! :)

    def progress(value):
        return HTML(
            f"""
            <progress value='{value}' max="100", style='width: 100%'>
                {value}
            </progress>
        """
        )

    progress_bar = display(progress(0), display_id=True)

    try:
        import google.colab

        using_colab = True
    except ImportError:
        using_colab = False

    if using_colab:
        with open("frame-buffer", "w") as writefile:
            writefile.write(
                """#taken from https://gist.github.com/jterrace/2911875
        XVFB=/usr/bin/Xvfb
        XVFBARGS=":1 -screen 0 1024x768x24 -ac +extension GLX +render -noreset"
        PIDFILE=./frame-buffer.pid
        case "$1" in
        start)
            /sbin/start-stop-daemon --start --quiet --pidfile $PIDFILE --make-pidfile --background --exec $XVFB -- $XVFBARGS
            ;;
        stop)
            /sbin/start-stop-daemon --stop --quiet --pidfile $PIDFILE
            rm $PIDFILE
            ;;
        restart)
            $0 stop
            $0 start
            ;;
        *)
                exit 1
        esac
        exit 0
            """
            )

        progress_bar.update(progress(5))
        os.system("apt-get install daemon >/dev/null 2>&1")

        progress_bar.update(progress(10))
        os.system("apt-get install wget >/dev/null 2>&1")

        progress_bar.update(progress(20))
        os.system(
            "wget http://ai2thor.allenai.org/ai2thor-colab/libxfont1_1.5.1-1ubuntu0.16.04.4_amd64.deb >/dev/null 2>&1"
        )

        progress_bar.update(progress(30))
        os.system(
            "wget --output-document xvfb.deb http://ai2thor.allenai.org/ai2thor-colab/xvfb_1.18.4-0ubuntu0.12_amd64.deb >/dev/null 2>&1"
        )

        progress_bar.update(progress(40))
        os.system("dpkg -i libxfont1_1.5.1-1ubuntu0.16.04.4_amd64.deb >/dev/null 2>&1")

        progress_bar.update(progress(50))
        os.system("dpkg -i xvfb.deb >/dev/null 2>&1")

        progress_bar.update(progress(70))
        os.system("rm libxfont1_1.5.1-1ubuntu0.16.04.4_amd64.deb")

        progress_bar.update(progress(80))
        os.system("rm xvfb.deb")

        progress_bar.update(progress(90))
        os.system("bash frame-buffer start")

        os.environ["DISPLAY"] = ":1"
    progress_bar.update(progress(100))
