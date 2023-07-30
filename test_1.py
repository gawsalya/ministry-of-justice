'''libraries required to filter/validate information'''
from datetime import datetime as dt


def is_log_line(line: str) -> bool:
    """Takes a log line and returns True if it is a valid log line and returns nothing
    if it is not.
    """
    error_types = ['INFO', 'WARNING', 'TRACE']

    separated_out = line.split()
    if len(separated_out) < 5:
        return None

    date = separated_out[0] + ' ' + separated_out[1]
    e_type = separated_out[2]
    message = ' '.join(separated_out[3:])
    try:
        dt.strptime(date, '%d/%m/%y %H:%M:%S')
    except:
        return None

    if e_type not in error_types:
        return None

    if ':' not in message:
        return None

    return True


def get_dict(line: str) -> dict:
    """Takes a log line and returns a dict with
    `timestamp`, `log_level`, `message` keys
    """
    separated_out = line.split()

    date_time = separated_out[0] + ' ' + separated_out[1]
    e_type = separated_out[2]
    message = ' '.join(separated_out[3:])

    formatted_line = {}
    formatted_line["timestamp"] = date_time
    formatted_line["log_level"] = e_type
    formatted_line["message"] = message

    return formatted_line


# YOU DON'T NEED TO CHANGE ANYTHING BELOW THIS LINE
if __name__ == "__main__":
    # these are basic generators that will return
    # 1 line of the log file at a time
    def log_parser_step_1(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield line

    def log_parser_step_2(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield get_dict(line)

    # ---- OUTPUT --- #
    # You can print out each line of the log file line by line
    # by uncommenting this code below
    # for i, line in enumerate(log_parser("sample.log")):
    #    print(i, line)

    # ---- TESTS ---- #
    # DO NOT CHANGE

    def test_step_1():
        with open("tests/step1.log") as f:
            test_lines = f.readlines()
        actual_out = list(log_parser_step_1("sample.log"))

        if actual_out == test_lines:
            print("STEP 1 SUCCESS")
        else:
            print(
                "STEP 1 FAILURE: step 1 produced unexpecting lines.\n"
                "Writing to failure.log if you want to compare it to tests/step1.log"
            )
            with open("step-1-failure-output.log", "w") as f:
                f.writelines(actual_out)

    def test_step_2():
        expected = {
            "timestamp": "03/11/21 08:51:01",
            "log_level": "INFO",
            "message": ":.main: *************** RSVP Agent started ***************",
        }
        actual = next(log_parser_step_2("sample.log"))

        if expected == actual:
            print("STEP 2 SUCCESS")
        else:
            print(
                "STEP 2 FAILURE: your first item from the generator was not as expected.\n"
                "Printing both expected and your output:\n"
            )
            print(f"Expected: {expected}")
            print(f"Generator Output: {actual}")

    try:
        test_step_1()
    except Exception:
        print("step 1 test unable to run")

    try:
        test_step_2()
    except Exception:
        print("step 2 test unable to run")
