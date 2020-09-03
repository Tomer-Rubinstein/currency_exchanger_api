import requests

class Currency:
    """
    TODO:
     - BUG: if date return " " (none): check if few days before gives a result + print this date
    """
    def __init__(self, c_code, date):
        self.c_code = c_code
        self.date = date

    def get_currency(self):
        """
        PARAMS: 
        - c_code = Currency Code: String (01 = usd, 27 = euro)
        RETURN:
        - XML section of the currency
        """
        curr = f"https://www.boi.org.il/currency.xml?rdate={self.date}&curr={self.c_code}"
        r = requests.get(curr)
        return r.text

    @staticmethod
    def get_value(xml):
        """
        PARAMS: 
        - xml = XML: XML (The xml section of the currency)
        RETURN:
        - Value of currency in ILS format (default)
        """
        raw_xml = xml.split()
        line = ""
        for tag in raw_xml:
            if "<RATE>" in tag:
                line = tag
        line = line.replace("<RATE>", "")
        line = line.replace("</RATE>", "")
        return line

USD = Currency("01", "20200902")
print(USD.get_value(USD.get_currency()))
