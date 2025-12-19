import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

# ================= LOGGING CONFIG =================
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s"
)

logger = logging.getLogger(__name__)


# ================= MODEL =================
@dataclass
class Student:
    """Representasi data mahasiswa.

    Attributes:
        name (str): Nama mahasiswa.
        sks (int): Jumlah SKS yang diambil.
        has_prerequisite (bool): Status pemenuhan prasyarat.
    """
    name: str
    sks: int
    has_prerequisite: bool


# ================= ABSTRAKSI =================
class IValidationRule(ABC):
    """Interface untuk semua aturan validasi registrasi."""

    @abstractmethod
    def validate(self, student: Student) -> bool:
        """Melakukan validasi terhadap data mahasiswa.

        Args:
            student (Student): Data mahasiswa yang akan divalidasi.

        Returns:
            bool: True jika valid, False jika tidak.
        """
        pass


# ================= IMPLEMENTASI RULE =================
class SksLimitRule(IValidationRule):
    """Validasi batas maksimum SKS."""

    MAX_SKS = 24

    def validate(self, student: Student) -> bool:
        if student.sks > self.MAX_SKS:
            logger.warning(
                "Validasi gagal: %s mengambil SKS melebihi batas (%d)",
                student.name, student.sks
            )
            return False

        logger.info(
            "Validasi SKS berhasil untuk %s (%d SKS)",
            student.name, student.sks
        )
        return True


class PrerequisiteRule(IValidationRule):
    """Validasi pemenuhan prasyarat mata kuliah."""

    def validate(self, student: Student) -> bool:
        if not student.has_prerequisite:
            logger.warning(
                "Validasi gagal: %s belum memenuhi prasyarat",
                student.name
            )
            return False

        logger.info(
            "Validasi prasyarat berhasil untuk %s",
            student.name
        )
        return True


# ================= SERVICE =================
class RegistrationService:
    """Service untuk memproses validasi registrasi mahasiswa.

    Class ini bertanggung jawab untuk:
    - Mengelola aturan validasi
    - Menjalankan proses registrasi
    """

    def __init__(self, rules: List[IValidationRule]):
        """Inisialisasi RegistrationService.

        Args:
            rules (List[IValidationRule]): Daftar aturan validasi.
        """
        self.rules = rules

    def register(self, student: Student) -> bool:
        """Menjalankan proses registrasi mahasiswa.

        Args:
            student (Student): Mahasiswa yang akan diregistrasi.

        Returns:
            bool: True jika registrasi berhasil, False jika gagal.
        """
        logger.info("Memulai registrasi untuk mahasiswa: %s", student.name)

        for rule in self.rules:
            if not rule.validate(student):
                logger.warning(
                    "Registrasi mahasiswa %s gagal",
                    student.name
                )
                return False

        logger.info(
            "Registrasi mahasiswa %s berhasil",
            student.name
        )
        return True


# ================= PROGRAM UTAMA =================
rules = [
    SksLimitRule(),
    PrerequisiteRule()
]

registration_service = RegistrationService(rules)

student1 = Student("Andi", 20, True)
student2 = Student("Budi", 26, False)

registration_service.register(student1)
registration_service.register(student2)
