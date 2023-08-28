from .connector import BF4PyConnector
from datetime import date
from .general import eod_data

class Bonds():
    def __init__(self, connector: BF4PyConnector = None, default_isin=None):
        self.default_isin = default_isin

        if connector is None:
            self.connector = BF4PyConnector()
        else:
            self.connector = connector

    def bond_details(self, isin: str = None):
        """
        Get detailed data about specific bond (by ISIN).

        Parameters
        ----------
        isin : str
            Desired ISIN.

        Returns
        -------
        data : TYPE
            Dict with data.

        """
        if isin is None:
            isin = self.default_isin
        assert isin is not None, "No ISIN given"

        params = {"isin": isin}

        data = self.connector.data_request("master_data_bond", params)

        return data

    def bond_basic_information(self, isin: str = None):
        """
        Get basic data about specific bond (by ISIN) including Mic.

        Parameters
        ----------
        isin : str
            Desired ISIN.

        Returns
        -------
        data : TYPE
            Dict with data.

        """
        if isin is None:
            isin = self.default_isin
        assert isin is not None, "No ISIN given"

        params = {"isin": isin}

        data = self.connector.data_request("instrument_information", params)

        return data

    # def bond_eod(self, min_date: date, max_date: date=date.today(), isin: str = None, mic:str='XFRA'):
    #     return eod_data(min_date: date, max_date: date=date.today(), isin: str = None, mic:str)
    
