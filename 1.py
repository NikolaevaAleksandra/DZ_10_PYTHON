import time
class TrafficLight:
    color = 'red'
    def running(self):
        print (TrafficLight.color)
        time.sleep(7)
        print('yellow')
        time.sleep(3)
        print('green')
        time.sleep(5)
        tr=TrafficLight()
        tr.running()
        
    