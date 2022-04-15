from abc import ABC, abstractmethod


class FileHandler:
    def open_file(self, path: str):
        # file.open()
        return path.split(".")[0]

    def close_file(self, file) -> bool:
        # file.close()
        return True


class DataMiner(ABC):
    # this should be final method
    def algorithm(self, path) -> None:
        file_handler = FileHandler()

        file = file_handler.open_file(path)

        raw_data = self.extract_data(file)

        data = self.parse_file(raw_data)

        analysis = self.analyze_data(data)

        self.send_report(analysis)

        file_handler.close_file(file)

    @abstractmethod
    def extract_data(self, file) -> str:
        ...

    @abstractmethod
    def parse_file(self, raw_data) -> str:
        ...

    def analyze_data(self, data):
        print(f"Analysing data: {data}")

        return data

    # hook
    def send_report(self, analysis) -> None:
        ...


class CSVMiner(DataMiner):
    def extract_data(self, file) -> str:
        print(f"Extracting CSV from {file}")

        return f"{file}_data"

    def parse_file(self, raw_data) -> str:
        print(f"Parsing raw CSV data: {raw_data}")

        return f"{raw_data}_parsed_csv"


class PDFMiner(DataMiner):
    def extract_data(self, file) -> str:
        print(f"Extracting PDF from {file}")

        return f"{file}_data"

    def parse_file(self, raw_data) -> str:
        print(f"Parsing raw PDF data: {raw_data}")

        return f"{raw_data}_parsed_pdf"

    def analyze_data(self, data):
        return data

    def send_report(self, analysis):
        print(f"Our report shows that the current data for... {analysis}")
