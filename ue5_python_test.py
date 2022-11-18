"""Testing python in UE5.

To see where UE5 is running from, you can run:

import os
print(f"We are currently at {os.getcwd()}")

To runpy  this script in UE5, you can run:

py "PATH_TO_THIS_FILE" --num=10000

"""

import argparse
import time
import foo_module
import unreal

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--num', type=int, default=1, help='Number of times to calculate.')


if __name__ == '__main__':
    args = parser.parse_args()

    # Show how we can import our own made up module
    print(f"From foo_module: {foo_module.answer}")

    # Do some time consuming work
    start_time = time.time()
    for i in range(args.num):
        _ = i * i * i
    end_time = time.time()
    total_time = end_time - start_time
    print(f'Calculated {args.num} times in {total_time:.6f} seconds.')
    
    # Unreal module can be used nicely
    unreal.log("Hello from Python!")
    print(f"Type of unreal.Array(str) in Python is {type(unreal.Array(str))}")
    print(f"Type of unreal.Map(str, bool) in Python is {type(unreal.Map(str, bool))}")
    my_dict = unreal.Map(str, str)
    my_dict['foo'] = 'bar'
    print(f"Type of my_dict['foo'] in Python is {type(my_dict)}")

    # Create objects in the editor
    text = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.FloatingText, unreal.Vector(0, 0, 0))
    with unreal.ScopedEditorTransaction("Move our FloatingText") as trans:
        text.set_actor_location(unreal.Vector(0, 0, 1), False, False)

    # Loading bars!
    with unreal.ScopedSlowTask(100, "Doing some work") as slow_task:
        slow_task.make_dialog(True)
        for i in range(100):
            slow_task.enter_progress_frame(1)
            time.sleep(0.01)





















