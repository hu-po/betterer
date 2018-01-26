# Command pattern
# 3 components
# - Client - Creates the instance
# - Invoker - Calls the methods
# - Receiver - Executes the method calls

class Switch(object):
    """ The Invoker class """

    def __init__(self, flipUpCmd, flipDownCmd):
        self._flipUpCmd = flipUpCmd
        self._flipDownCmd = flipDownCmd

    def flipUp(self):
        self._flipUpCmd.execute()

    def flipDown(self):
        self._flipDownCmd.execute()


class Light(object):
    """ The Receiver """

    def turnOn(self):
        print('Light is on')

    def turnOff(self):
        print('Light is off')


class FlipUpCommand(object):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turnOn()


class FlipDownCommand(object):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turnOff()

class LightSwitch(object):
    """ The Client """

    def __init__(self):
        self._lamp = Light()
        self._switchUp = FlipUpCommand(self._lamp)
        self._switchDown = FlipDownCommand(self._lamp)
        self._switch = Switch(self._switchUp, self._switchDown)

    def switch(self, cmd):
        cmd = cmd.strip().upper()
        try:
            if cmd == 'ON':
                self._switch.flipUp()
            elif cmd == 'OFF':
                self._switch.flipDown()
            else:
                print('Invalid command')
        except Exception as e:
            print('Exception %s occured in Lightswitch' % e)

if __name__ == '__main__':

    lightSwitch = LightSwitch()

    lightSwitch.switch('ON')

    lightSwitch.switch('OFF')

    lightSwitch.switch('OFF')

    lightSwitch.switch('ON')
