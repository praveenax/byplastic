from time import strftime

class currentdatetime:

    @staticmethod
    def get_current_time_stamp():
        return strftime("%Y-%m-%d %H:%M:%S")
