"""
    Dashboard Deutschland API

    Auf https://www.dashboard-deutschland.de bietet das Statistische Bundesamt DESTATIS einen Überblick zu gesellschaftlich und wirtschaftlich relevanten Daten aus unterschiedlichen Themenbereichen. Diese werden durch Grafiken und Texte ergänzt und regelmäßig aktualisiert. Damit soll eine Möglichkeit geboten werden, aktuelle Kennzahlen und deren Entwicklung übersichtlich darzustellen.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.DashboardDeutschland.model.geo_crs import GeoCrs

from deutschland import DashboardDeutschland

globals()["GeoCrs"] = GeoCrs
from deutschland.DashboardDeutschland.model.geo import Geo


class TestGeo(unittest.TestCase):
    """Geo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGeo(self):
        """Test Geo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Geo()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
