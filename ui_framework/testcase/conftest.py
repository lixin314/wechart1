import os
import signal
import subprocess
import pytest


@pytest.fixture(scope='module', autouse=True)
def record():
    video_path = os.getcwd() + "\\result\\"
    video_name = video_path + 'mp4.mp4'
    cmd = f"scrcpy -Nr {video_name}"
    p = subprocess.Popen(cmd, shell=True)

    yield

    os.kill(p.pid, signal.CTRL_C_EVENT)


