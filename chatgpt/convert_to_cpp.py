
# Convert to C++

@dataclass
class Robot:
    name: str
    camera: Camera
    x: int = 0
    y: int = 0

    def take_picture(self):
        return self.camera.take_picture()

    def move(self, x, y):
        self.x += x
        self.y += y

#include <iostream>
#include <string>

using namespace std;

class Camera {
public:
string take_picture() {
return "picture taken";
}
};

class Robot {
private:
string name;
Camera camera;
int x = 0;
int y = 0;
public:
Robot(string name, Camera camera) : name(name), camera(camera) {};

Copy code
string take_picture() {
    return camera.take_picture();
}

void move(int x, int y) {
    this->x += x;
    this->y += y;
}
};

int main() {
Camera camera;
Robot robot("Robot1", camera);

Copy code
cout << robot.take_picture() << endl;
robot.move(10, 5);

return 0;
}