import threading, playsound, time, sys, ctypes

game_state = 0
done = 0
global music_player


def music():
    while True:
        # State Variables
        global game_state
        global done
        state = ["Music\intro.mp3", "Music\mid.mp3", "Music\end.mp3"]
        timer = [6.81731, 10.182352, 22]

        # Stop if music disabled
        if done == 2:
            break

        # Play music on loop until end
        while game_state != 2:
            playsound.playsound(state[game_state], False)
            time.sleep(timer[game_state])
            if game_state == 0:
                game_state = 1

        # End and wait for start
        playsound.playsound("end.mp3", False)
        time.sleep(22)
        done = 1
        while game_state == 2:
            pass


# Define Treading Class for Music
class MyThread(threading.Thread):
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name

    def run(self):
        music()

    def get_id(self):

        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')


def start():
    global game_state, music_player, done
    game_state = 0

    if done != 2:
        done = 0

    # Create new Thread
    music_player = MyThread(1, "Music_Player")

    # Start new Thread
    music_player.start()


def kill():
    global music_player
    music_player.raise_exception()
    music_player.join()
