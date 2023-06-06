import time
import functools
import inspect
import subprocess

import time
import functools
import inspect
import subprocess


def print_method_name(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Метод: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


def measure_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Метод: {func.__name__}, Час виконання: {execution_time} сек")
        return result
    return wrapper


def count_method_calls(func):
    call_count = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if func.__name__ not in call_count:
            call_count[func.__name__] = 1
        else:
            call_count[func.__name__] += 1

        with open("method_calls.txt", "a") as file:
            file.write(f"Метод: {func.__name__}, Кількість викликів: {call_count[func.__name__]}\n")

        return func(*args, **kwargs)
    return wrapper


def log_input_output(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with open("method_logs.txt", "a") as file:
            file.write(f"Метод: {func.__name__}, Вхідні параметри: args={args}, kwargs={kwargs}\n")

        result = func(*args, **kwargs)

        with open("method_logs.txt", "a") as file:
            file.write(f"Метод: {func.__name__}, Вихідне значення: {result}\n")

        return result
    return wrapper


def save_call_history(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with open("call_history.txt", "a") as file:
            file.write(f"Метод: {func.__name__}, Час виклику: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        return func(*args, **kwargs)
    return wrapper


def check_argument_count(func):
    expected_arg_count = len(inspect.signature(func).parameters)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        actual_arg_count = len(args) + len(kwargs)
        if actual_arg_count != expected_arg_count:
            raise ValueError(f"Неправильна кількість аргументів для методу {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


def write_keyword_arguments(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with open("keyword_arguments.txt", "a") as file:
            for key, value in kwargs.items():
                file.write(f"{func.__name__}: {key}={value}\n")
        return func(*args, **kwargs)
    return wrapper


def log_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            with open("exceptions.txt", "a") as file:
                file.write(f"Метод: {func.__name__}, Виключення: {e}\n")
    return wrapper


def limit_method_calls(max_calls):
    call_count = {}

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if func.__name__ not in call_count:
                call_count[func.__name__] = 1
            else:
                call_count[func.__name__] += 1

            if call_count[func.__name__] > max_calls:
                raise Exception("Занадто багато викликів")

            return func(*args, **kwargs)
        return wrapper
    return decorator


def enforce_python_naming_convention(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        method_name = func.__name__
        if not method_name.islower() or "_" in method_name:
            raise ValueError(f"Назва методу {method_name} не відповідає Python-конвенції")
        return func(*args, **kwargs)
    return wrapper


def print_iterable_length(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if hasattr(result, "__iter__"):
            print(f"Метод: {func.__name__}, Довжина ітеративного об'єкту: {len(result)}")
        else:
            print(f"Метод: {func.__name__}, Довжина об'єкту: 1")
        return result
    return wrapper


def save_result_to_file(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        filename = f"{func.__qualname__}.txt"
        with open(filename, "w") as file:
            result = func(*args, **kwargs)
            file.write(str(result))
        return result
    return wrapper


def convert_iterator_to_tuple(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if hasattr(result, "__iter__"):
            result = tuple(result)
        return result
    return wrapper


def run_pylint(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        filename = inspect.getsourcefile(func)
        subprocess.run(["pylint", filename])
        return func(*args, **kwargs)
    return wrapper


@print_method_name
@measure_execution_time
@count_method_calls
@log_input_output
@save_call_history
@check_argument_count
@write_keyword_arguments
@log_exceptions
@limit_method_calls(3)
@enforce_python_naming_convention
@print_iterable_length
@save_result_to_file
@convert_iterator_to_tuple
@run_pylint
class InsectManager:
    def __init__(self):
        self.insects = []

    def add_insect(self, insect):
        self.insects.append(insect)

    def find_insects_by_number_of_legs(self, number_of_legs):
        return [insect for insect in self.insects if insect.get_number_of_legs() == number_of_legs]

    def find_insects_that_can_inject_poison(self):
        return [insect for insect in self.insects if insect.can_inject_poison()]

    def __len__(self):
        return len(self.insects)

    def __getitem__(self, index):
        return self.insects[index]

    def __iter__(self):
        return iter(self.insects)

    def get_results_of_survive_over_winter(self):
        return [insect.survive_over_winter() for insect in self.insects]

    def get_numbered_objects(self):
        return list(enumerate(self.insects))

    def get_pairs_with_survival_results(self):
        return list(zip(self.insects, self.get_results_of_survive_over_winter()))

    def get_attributes_by_type(self, attribute_type):
        return {key: value for key, value in self.insects[0].__dict__.items() if isinstance(value, attribute_type)}

    def check_conditions(self, condition):
        return {"all": all(condition(insect) for insect in self.insects),
                "any": any(condition(insect) for insect in self.insects)}

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def add_insect(self, insect):
        self.insects.append(insect)

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def find_insects_by_number_of_legs(self, number_of_legs):
        return [insect for insect in self.insects if insect.get_number_of_legs() == number_of_legs]

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def find_insects_that_can_inject_poison(self):
        return [insect for insect in self.insects if insect.can_inject_poison()]

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def __len__(self):
        return len(self.insects)

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def __getitem__(self, index):
        return self.insects[index]

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def __iter__(self):
        return iter(self.insects)

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def get_results_of_survive_over_winter(self):
        return [insect.survive_over_winter() for insect in self.insects]

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def get_numbered_objects(self):
        return list(enumerate(self.insects))

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def get_pairs_with_survival_results(self):
        return list(zip(self.insects, self.get_results_of_survive_over_winter()))

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def get_attributes_by_type(self, attribute_type):
        return {key: value for key, value in self.insects[0].__dict__.items() if isinstance(value, attribute_type)}

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def check_conditions(self, condition):
        return {"all": all(condition(insect) for insect in self.insects),
                "any": any(condition(insect) for insect in self.insects)}

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def get_results_of_survive_over_winter(self):
        return [insect.survive_over_winter() for insect in self.insects]

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def get_numbered_objects(self):
        return list(enumerate(self.insects))

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def get_pairs_with_survival_results(self):
        return list(zip(self.insects, self.get_results_of_survive_over_winter()))

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def get_attributes_by_type(self, attribute_type):
        return {key: value for key, value in self.insects[0].__dict__.items() if isinstance(value, attribute_type)}

    @print_method_name
    @measure_execution_time
    @count_method_calls
    @log_input_output
    @save_call_history
    def check_conditions(self, condition):
        return {"all": all(condition(insect) for insect in self.insects),
                "any": any(condition(insect) for insect in self.insects)}
