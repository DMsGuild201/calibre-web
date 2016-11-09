'''tzinfo timezone information for America/Goose_Bay.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Goose_Bay(DstTzInfo):
    '''America/Goose_Bay timezone definition. See datetime.tzinfo for details'''

    zone = 'America/Goose_Bay'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1918,4,14,5,30,52),
d(1918,10,31,4,30,52),
d(1935,3,30,3,30,52),
d(1936,5,11,3,30,0),
d(1936,10,5,2,30,0),
d(1937,5,10,3,30,0),
d(1937,10,4,2,30,0),
d(1938,5,9,3,30,0),
d(1938,10,3,2,30,0),
d(1939,5,15,3,30,0),
d(1939,10,2,2,30,0),
d(1940,5,13,3,30,0),
d(1940,10,7,2,30,0),
d(1941,5,12,3,30,0),
d(1941,10,6,2,30,0),
d(1942,5,11,3,30,0),
d(1945,8,14,23,0,0),
d(1945,9,30,4,30,0),
d(1946,5,12,5,30,0),
d(1946,10,6,4,30,0),
d(1947,5,11,5,30,0),
d(1947,10,5,4,30,0),
d(1948,5,9,5,30,0),
d(1948,10,3,4,30,0),
d(1949,5,8,5,30,0),
d(1949,10,2,4,30,0),
d(1950,5,14,5,30,0),
d(1950,10,8,4,30,0),
d(1951,4,29,5,30,0),
d(1951,9,30,4,30,0),
d(1952,4,27,5,30,0),
d(1952,9,28,4,30,0),
d(1953,4,26,5,30,0),
d(1953,9,27,4,30,0),
d(1954,4,25,5,30,0),
d(1954,9,26,4,30,0),
d(1955,4,24,5,30,0),
d(1955,9,25,4,30,0),
d(1956,4,29,5,30,0),
d(1956,9,30,4,30,0),
d(1957,4,28,5,30,0),
d(1957,9,29,4,30,0),
d(1958,4,27,5,30,0),
d(1958,9,28,4,30,0),
d(1959,4,26,5,30,0),
d(1959,9,27,4,30,0),
d(1960,4,24,5,30,0),
d(1960,10,30,4,30,0),
d(1961,4,30,5,30,0),
d(1961,10,29,4,30,0),
d(1962,4,29,5,30,0),
d(1962,10,28,4,30,0),
d(1963,4,28,5,30,0),
d(1963,10,27,4,30,0),
d(1964,4,26,5,30,0),
d(1964,10,25,4,30,0),
d(1965,4,25,5,30,0),
d(1965,10,31,4,30,0),
d(1966,3,15,5,30,0),
d(1966,4,24,6,0,0),
d(1966,10,30,5,0,0),
d(1967,4,30,6,0,0),
d(1967,10,29,5,0,0),
d(1968,4,28,6,0,0),
d(1968,10,27,5,0,0),
d(1969,4,27,6,0,0),
d(1969,10,26,5,0,0),
d(1970,4,26,6,0,0),
d(1970,10,25,5,0,0),
d(1971,4,25,6,0,0),
d(1971,10,31,5,0,0),
d(1972,4,30,6,0,0),
d(1972,10,29,5,0,0),
d(1973,4,29,6,0,0),
d(1973,10,28,5,0,0),
d(1974,4,28,6,0,0),
d(1974,10,27,5,0,0),
d(1975,4,27,6,0,0),
d(1975,10,26,5,0,0),
d(1976,4,25,6,0,0),
d(1976,10,31,5,0,0),
d(1977,4,24,6,0,0),
d(1977,10,30,5,0,0),
d(1978,4,30,6,0,0),
d(1978,10,29,5,0,0),
d(1979,4,29,6,0,0),
d(1979,10,28,5,0,0),
d(1980,4,27,6,0,0),
d(1980,10,26,5,0,0),
d(1981,4,26,6,0,0),
d(1981,10,25,5,0,0),
d(1982,4,25,6,0,0),
d(1982,10,31,5,0,0),
d(1983,4,24,6,0,0),
d(1983,10,30,5,0,0),
d(1984,4,29,6,0,0),
d(1984,10,28,5,0,0),
d(1985,4,28,6,0,0),
d(1985,10,27,5,0,0),
d(1986,4,27,6,0,0),
d(1986,10,26,5,0,0),
d(1987,4,5,4,1,0),
d(1987,10,25,3,1,0),
d(1988,4,3,4,1,0),
d(1988,10,30,2,1,0),
d(1989,4,2,4,1,0),
d(1989,10,29,3,1,0),
d(1990,4,1,4,1,0),
d(1990,10,28,3,1,0),
d(1991,4,7,4,1,0),
d(1991,10,27,3,1,0),
d(1992,4,5,4,1,0),
d(1992,10,25,3,1,0),
d(1993,4,4,4,1,0),
d(1993,10,31,3,1,0),
d(1994,4,3,4,1,0),
d(1994,10,30,3,1,0),
d(1995,4,2,4,1,0),
d(1995,10,29,3,1,0),
d(1996,4,7,4,1,0),
d(1996,10,27,3,1,0),
d(1997,4,6,4,1,0),
d(1997,10,26,3,1,0),
d(1998,4,5,4,1,0),
d(1998,10,25,3,1,0),
d(1999,4,4,4,1,0),
d(1999,10,31,3,1,0),
d(2000,4,2,4,1,0),
d(2000,10,29,3,1,0),
d(2001,4,1,4,1,0),
d(2001,10,28,3,1,0),
d(2002,4,7,4,1,0),
d(2002,10,27,3,1,0),
d(2003,4,6,4,1,0),
d(2003,10,26,3,1,0),
d(2004,4,4,4,1,0),
d(2004,10,31,3,1,0),
d(2005,4,3,4,1,0),
d(2005,10,30,3,1,0),
d(2006,4,2,4,1,0),
d(2006,10,29,3,1,0),
d(2007,3,11,4,1,0),
d(2007,11,4,3,1,0),
d(2008,3,9,4,1,0),
d(2008,11,2,3,1,0),
d(2009,3,8,4,1,0),
d(2009,11,1,3,1,0),
d(2010,3,14,4,1,0),
d(2010,11,7,3,1,0),
d(2011,3,13,4,1,0),
d(2011,11,6,3,1,0),
d(2012,3,11,4,1,0),
d(2012,11,4,3,1,0),
d(2013,3,10,4,1,0),
d(2013,11,3,3,1,0),
d(2014,3,9,4,1,0),
d(2014,11,2,3,1,0),
d(2015,3,8,4,1,0),
d(2015,11,1,3,1,0),
d(2016,3,13,4,1,0),
d(2016,11,6,3,1,0),
d(2017,3,12,4,1,0),
d(2017,11,5,3,1,0),
d(2018,3,11,4,1,0),
d(2018,11,4,3,1,0),
d(2019,3,10,4,1,0),
d(2019,11,3,3,1,0),
d(2020,3,8,4,1,0),
d(2020,11,1,3,1,0),
d(2021,3,14,4,1,0),
d(2021,11,7,3,1,0),
d(2022,3,13,4,1,0),
d(2022,11,6,3,1,0),
d(2023,3,12,4,1,0),
d(2023,11,5,3,1,0),
d(2024,3,10,4,1,0),
d(2024,11,3,3,1,0),
d(2025,3,9,4,1,0),
d(2025,11,2,3,1,0),
d(2026,3,8,4,1,0),
d(2026,11,1,3,1,0),
d(2027,3,14,4,1,0),
d(2027,11,7,3,1,0),
d(2028,3,12,4,1,0),
d(2028,11,5,3,1,0),
d(2029,3,11,4,1,0),
d(2029,11,4,3,1,0),
d(2030,3,10,4,1,0),
d(2030,11,3,3,1,0),
d(2031,3,9,4,1,0),
d(2031,11,2,3,1,0),
d(2032,3,14,4,1,0),
d(2032,11,7,3,1,0),
d(2033,3,13,4,1,0),
d(2033,11,6,3,1,0),
d(2034,3,12,4,1,0),
d(2034,11,5,3,1,0),
d(2035,3,11,4,1,0),
d(2035,11,4,3,1,0),
d(2036,3,9,4,1,0),
d(2036,11,2,3,1,0),
d(2037,3,8,4,1,0),
d(2037,11,1,3,1,0),
        ]

    _transition_info = [
i(-12660,0,'NST'),
i(-9060,3600,'NDT'),
i(-12660,0,'NST'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NWT'),
i(-9000,3600,'NPT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-9000,3600,'NDT'),
i(-12600,0,'NST'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-7200,7200,'ADDT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
i(-10800,3600,'ADT'),
i(-14400,0,'AST'),
        ]

Goose_Bay = Goose_Bay()
