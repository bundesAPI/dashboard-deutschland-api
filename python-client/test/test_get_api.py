"""
    Dashboard Deutschland API

    Auf https://www.dashboard-deutschland.de bietet das Statistische Bundesamt DESTATIS einen Überblick zu gesellschaftlich und wirtschaftlich relevanten Daten aus unterschiedlichen Themenbereichen. Diese werden durch Grafiken und Texte ergänzt und regelmäßig aktualisiert. Damit soll eine Möglichkeit geboten werden, aktuelle Kennzahlen und deren Entwicklung übersichtlich darzustellen.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""

import unittest

from deutschland.DashboardDeutschland.api.get_api import GetApi  # noqa: E501

from deutschland import DashboardDeutschland


class TestGetApi(unittest.TestCase):
    """GetApi unit test stubs"""

    def setUp(self):
        self.api = GetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get(self):
        """Test case for get

        Zugriff auf alle gültigen Einträge des id-Parameters  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
