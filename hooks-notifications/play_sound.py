import os
import sys
import winsound


def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sound_file = os.path.join(script_dir, "notification.wav")

    # Play the notification sound
    if os.path.exists(sound_file):
        print(f"Playing notification sound: {sound_file}")
        try:
            winsound.PlaySound(sound_file, winsound.SND_FILENAME)
            print("Sound played successfully!")
        except Exception as e:
            print(f"Error playing sound: {e}")
            sys.exit(1)
    else:
        print(f"Error: Sound file not found at {sound_file}")
        sys.exit(1)


if __name__ == "__main__":
    main()
