"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .abbvie import AbbvieFetcher
from .astrazeneca import AstrazenecaFetcher
from .bora import BoraFetcher
from .cardinal import CardinalFetcher
from .catalent import CatalentFetcher
from .cencora import CencoraFetcher
from .dr_reddy import DrReddyFetcher
from .eli_lilly import EliLillyFetcher
from .jnj import JnjFetcher
from .lonza import LonzaFetcher
from .mckesson import MckessonFetcher
from .merck import MerckFetcher
from .novartis import NovartisFetcher
from .novo_nordisk import NovoNordiskFetcher
from .pfizer import PfizerFetcher
from .roche import RocheFetcher
from .sanofi import SanofiFetcher
from .sun_pharma import SunPharmaFetcher
from .tci import TciFetcher
from .teva import TevaFetcher

FETCHERS = {
    "abbvie": AbbvieFetcher,
    "astrazeneca": AstrazenecaFetcher,
    "bora": BoraFetcher,
    "cardinal": CardinalFetcher,
    "catalent": CatalentFetcher,
    "cencora": CencoraFetcher,
    "dr_reddy": DrReddyFetcher,
    "eli_lilly": EliLillyFetcher,
    "jnj": JnjFetcher,
    "lonza": LonzaFetcher,
    "mckesson": MckessonFetcher,
    "merck": MerckFetcher,
    "novartis": NovartisFetcher,
    "novo_nordisk": NovoNordiskFetcher,
    "pfizer": PfizerFetcher,
    "roche": RocheFetcher,
    "sanofi": SanofiFetcher,
    "sun_pharma": SunPharmaFetcher,
    "tci": TciFetcher,
    "teva": TevaFetcher,
}
