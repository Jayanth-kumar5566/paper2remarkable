# -*- coding: utf-8 -*-

from .acl import ACL
from .acm import ACM
from .arxiv import Arxiv
from .citeseerx import CiteSeerX
from .cvf import CVF
from .eccc import ECCC
from .html import HTML
from .iacr import IACR
from .jmlr import JMLR
from .local import LocalFile
from .nature import Nature
from .nber import NBER
from .neurips import NeurIPS
from .openreview import OpenReview
from .pdf_url import PdfUrl
from .pmlr import PMLR
from .pubmed import PubMed
from .sagepub import SagePub
from .science_direct import ScienceDirect
from .semantic_scholar import SemanticScholar
from .springer import Springer

# NOTE: Order matters here, PdfUrl and HTML should be last
providers = [
    ACL,
    ACM,
    Arxiv,
    CiteSeerX,
    CVF,
    ECCC,
    IACR,
    JMLR,
    Nature,
    NBER,
    NeurIPS,
    OpenReview,
    PMLR,
    PubMed,
    SagePub,
    ScienceDirect,
    Springer,
    SemanticScholar,
    LocalFile,
    PdfUrl,
    HTML,
]
