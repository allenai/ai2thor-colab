from IPython.display import HTML, display
import os


def progress_bar(percentage_done: int):
    """Display a green progress loading bar.

    @param percentage_done is the current percentage of progress, in [0:100].
    """
    if percentage_done < 0 or percentage_done > 100:
        raise ValueError("value must be in [0:100]. You gave " + percentage_done)
    return HTML(
        f"""
        <progress
            value="{percentage_done}"
            max="100",
            style="width: 100%"
        >
            {percentage_done}
        </progress>"""
    )


def start_server():
    progress_display = display(progress_bar(percentage_done=0), display_id=True)
    try:
        import google.colab

        using_colab = True
    except:
        using_colab = False

    if using_colab:
        with open("frame-buffer", "w") as writefile:
            # credit for much of this goes to
            # https://gist.github.com/jterrace/2911875
            # and several other Colab notebooks that have started an XVFB in Colab :)
            writefile.write(
                """
XVFB=/usr/bin/Xvfb
XVFBARGS=":1 -screen 0 1024x768x24 -ac +extension GLX +render -noreset"
PIDFILE=./frame-buffer.pid
case "$1" in
start)
echo -n "Starting virtual X frame buffer: Xvfb"
/sbin/start-stop-daemon --start --quiet --pidfile $PIDFILE --make-pidfile --background --exec $XVFB -- $XVFBARGS
echo "."
;;
stop)
echo -n "Stopping virtual X frame buffer: Xvfb"
/sbin/start-stop-daemon --stop --quiet --pidfile $PIDFILE
rm $PIDFILE
echo "."
;;
restart)
$0 stop
$0 start
;;
*)
    echo "Usage: /etc/init.d/xvfb {start|stop|restart}"
    exit 1
esac
exit 0"""
            )
            progress_display.update(progress_bar(percentage_done=5))
            os.system("apt-get install daemon >/dev/null 2>&1")

            progress_display.update(progress_bar(percentage_done=10))
            os.system("apt-get install wget >/dev/null 2>&1")

            progress_display.update(progress_bar(percentage_done=20))
            os.system(
                "wget http://security.ubuntu.com/ubuntu/pool/main/libx/libxfont/libxfont1_1.5.1-1ubuntu0.16.04.4_amd64.deb >/dev/null 2>&1"
            )

            progress_display.update(progress_bar(percentage_done=30))
            os.system(
                "wget --output-document xvfb.deb http://security.ubuntu.com/ubuntu/pool/universe/x/xorg-server/xvfb_1.18.4-0ubuntu0.11_amd64.deb >/dev/null 2>&1"
            )

            progress_display.update(progress_bar(percentage_done=40))
            os.system(
                "dpkg -i libxfont1_1.5.1-1ubuntu0.16.04.4_amd64.deb >/dev/null 2>&1"
            )

            progress_display.update(progress_bar(percentage_done=50))
            os.system("dpkg -i xvfb.deb >/dev/null 2>&1")

            progress_display.update(progress_bar(percentage_done=70))
            os.system("rm libxfont1_1.5.1-1ubuntu0.16.04.4_amd64.deb")

            progress_display.update(progress_bar(percentage_done=80))
            os.system("rm xvfb.deb")

            progress_display.update(progress_bar(percentage_done=90))
            os.system("bash frame-buffer start")

            os.environ["DISPLAY"] = ":1"


def side_by_side():
    raise NotImplementedError()
