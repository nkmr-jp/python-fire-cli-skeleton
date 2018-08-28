import fire


class SampleCommand(object):
    """this is sample"""

    @staticmethod
    def hello():
        print("Hello world!")


def main():
    fire.Fire(SampleCommand)


if __name__ == "__main__":
    main()
