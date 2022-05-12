import cv2

class Room305dCommand:

    def __init__(self):
        self.help = """Use as \\room305d"""

    def __call__(self, params):
        """
        Take and send a picture of plants in the room.
        :return:
        """
        filepath = "figs/room305d.jpg"
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite(filepath, image)


        default_msg = [
            {"type": "fig", "filepath": filepath},
            {"type": "text", "text": "Rostliny v místnosti 305d."},
        ]
        # if params:
        #     default_msg += [{"type": "text", "text": "Used params: {}".format(params)},]
        return default_msg


if __name__ == "__main__":
    c = Room305dCommand()
    output = c.__call__("")

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)
        cv2.waitKey(1)

    cam.release()
    cv2.destroyAllWindows()