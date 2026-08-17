from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from database.database import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=True)
    resume_filename = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    claims = relationship(
        "Claim",
        back_populates="candidate",
        cascade="all, delete-orphan",
    )

    assessments = relationship(
        "Assessment",
        back_populates="candidate",
        cascade="all, delete-orphan",
    )

    proof_cards = relationship(
        "ProofCard",
        back_populates="candidate",
        cascade="all, delete-orphan",
    )


class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False,
    )
    skill = Column(String(100), nullable=False)
    source = Column(String(50), nullable=True)
    claim_text = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    candidate = relationship(
        "Candidate",
        back_populates="claims",
    )

    evidence = relationship(
        "Evidence",
        back_populates="claim",
        cascade="all, delete-orphan",
    )


class Evidence(Base):
    __tablename__ = "evidence"

    id = Column(Integer, primary_key=True, index=True)
    claim_id = Column(
        Integer,
        ForeignKey("claims.id"),
        nullable=False,
    )
    evidence_type = Column(String(50), nullable=False)
    reference = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    verified = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    claim = relationship(
        "Claim",
        back_populates="evidence",
    )


class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False,
    )
    skill = Column(String(100), nullable=False)
    session_id = Column(String(100), nullable=False, unique=True)
    status = Column(String(50), default="started", nullable=False)
    started_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    completed_at = Column(DateTime, nullable=True)

    candidate = relationship(
        "Candidate",
        back_populates="assessments",
    )

    evaluation = relationship(
        "Evaluation",
        back_populates="assessment",
        uselist=False,
        cascade="all, delete-orphan",
    )


class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)
    assessment_id = Column(
        Integer,
        ForeignKey("assessments.id"),
        nullable=False,
        unique=True,
    )
    score = Column(Float, nullable=True)
    result = Column(String(50), nullable=True)
    feedback = Column(Text, nullable=True)
    evaluated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    assessment = relationship(
        "Assessment",
        back_populates="evaluation",
    )

    proof_cards = relationship(
        "ProofCard",
        back_populates="evaluation",
    )


class ProofCard(Base):
    __tablename__ = "proof_cards"

    id = Column(Integer, primary_key=True, index=True)
    proof_card_id = Column(String(100), nullable=False, unique=True, index=True)
    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False,
    )
    evaluation_id = Column(
        Integer,
        ForeignKey("evaluations.id"),
        nullable=False,
    )
    skill = Column(String(100), nullable=False)
    score = Column(Float, nullable=True)
    status = Column(String(50), nullable=False)
    issued_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    integrity_hash = Column(String(64), nullable=False)

    candidate = relationship(
        "Candidate",
        back_populates="proof_cards",
    )

    evaluation = relationship(
        "Evaluation",
        back_populates="proof_cards",
    )