from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt"

class Log:
    def _log(self, msg):
        raise NotImplementedError("Implemente o método log")
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)
        msg_fomatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_fomatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_fomatada)
            arquivo.write('\n')
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')



if __name__ == "__main__":
    l = LogFileMixin()
    l.log_error ="qualquer coisa"
    l.log_success = "Boaaa"
    lf = LogPrintMixin()
    lf.log_error('qualquer coisa')
    lf.log_success('Que legal')