import queue
import traceback
from threading import Lock, Thread

STOP_THREADS = False


class ModbusThread(Thread):

    __modbus_lock = Lock()
    __modbus_task_queue = queue.LifoQueue()
    __modbus_results_queue = queue.Queue()
    __modbus_threads_number = 5

    def __init__(self, thread_id, task_queue):
        Thread.__init__(self, name="ModbusThread-%d" % (thread_id,))
        self.task_queue = task_queue

    def get_modbus_task_queue():
        return ModbusThread.__modbus_task_queue

    def get_modbus_results_queue():
        return ModbusThread.__modbus_results_queue

    def run(self):
        global STOP_THREADS

        while True:
            try:
                ModbusThread.__modbus_lock.acquire()

                request = self.task_queue.get()
                print("task queue inside thread", self.task_queue.qsize())

                if STOP_THREADS is True:
                    break

                functions_obj, device_id, results_queue = request
                result = ModbusThread.get_modbus_data_threaded(functions_obj, device_id)

                results_queue.put((device_id, result))

            except Exception as e:
                print("Exception!")
                print(e)
                traceback_str = "".join(traceback.format_tb(e.__traceback__))
                print(traceback_str)

            finally:
                self.task_queue.task_done()
                ModbusThread.__modbus_lock.release()

    def initialize_modbus_threads():
        for i in range(ModbusThread.__modbus_threads_number):
            new_thread = ModbusThread(i, ModbusThread.__modbus_task_queue)
            new_thread.setDaemon(True)
            new_thread.start()

    def get_modbus_data_threaded(functions_obj, device_id):
        response = None

        # time.sleep(0.3)

        functions_obj.reinitialize_modbus(device_id)

        response = functions_obj.get_modbus_device_data_routine(device_id)

        print("Modbus single response in thread", response)
        return response

    def terminate_all_threads():
        pass
