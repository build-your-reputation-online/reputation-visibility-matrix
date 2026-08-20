#!/usr/bin/env python3
"""
Reputation Visibility Matrix
A digital reputation analysis framework from BuildYourReputation.online,
created to help businesses, professionals, founders, and brands better
understand their online visibility and reputation signals.

Provides a structured framework for analyzing how a brand, business, or
individual appears across different areas of the digital landscape.

https://buildyourreputation.online
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def format_audit_type(audit_type: str) -> str:
    return " ".join(w.capitalize() for w in audit_type.split("-"))


def get_priority_action(scores: dict) -> str:
    labels = {
        "search_visibility": "Search Visibility",
        "mention": "Mention",
        "content": "Content",
        "media": "Media",
        "review": "Review",
        "digital_asset": "Digital Asset",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_reputation_channels(search: int, mention: int, review: int, media: int) -> dict:
    return {
        "Branded Search": min(100, round(search * 1.0)),
        "Social Mentions": min(100, round(mention * 1.0)),
        "Review Platforms": min(100, round(review * 1.0)),
        "Media Coverage": min(100, round(media * 1.0)),
    }


def run_reputation_matrix(
    brand: str,
    audit_type: str = "full-audit",
    search_visibility: int = 88,
    mention_score: int = 82,
    content_score: int = 85,
    media_score: int = 78,
    review_score: int = 90,
    digital_asset_score: int = 84,
) -> dict:
    """
    Run the Reputation Visibility Matrix across all reputation signals.

    Args:
        brand: Brand name or identifier
        audit_type: Type of reputation audit to run
        search_visibility: Branded search visibility score (0-100)
        mention_score: Online mention score (0-100)
        content_score: Published content score (0-100)
        media_score: Media reference score (0-100)
        review_score: Review signal score (0-100)
        digital_asset_score: Digital asset score (0-100)

    Returns:
        dict with individual signal scores, overall reputation index,
        and reputation channel breakdown
    """
    scores = {
        "search_visibility": search_visibility,
        "mention": mention_score,
        "content": content_score,
        "media": media_score,
        "review": review_score,
        "digital_asset": digital_asset_score,
    }
    overall_reputation_index = round(sum(scores.values()) / 6)

    return {
        "brand": brand,
        "audit_type": format_audit_type(audit_type),
        "search_visibility_score": search_visibility,
        "mention_score": mention_score,
        "content_score": content_score,
        "media_score": media_score,
        "review_score": review_score,
        "digital_asset_score": digital_asset_score,
        "overall_reputation_index": overall_reputation_index,
        "priority_action": get_priority_action(scores),
        "reputation_channels": get_reputation_channels(search_visibility, mention_score, review_score, media_score),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    brand = args[0] if len(args) > 0 else "brand-name"
    audit_type = args[1] if len(args) > 1 else "full-audit"
    search_visibility = int(args[2]) if len(args) > 2 else 88
    mention_score = int(args[3]) if len(args) > 3 else 82
    content_score = int(args[4]) if len(args) > 4 else 85
    media_score = int(args[5]) if len(args) > 5 else 78
    review_score = int(args[6]) if len(args) > 6 else 90
    digital_asset_score = int(args[7]) if len(args) > 7 else 84

    result = run_reputation_matrix(
        brand, audit_type, search_visibility, mention_score,
        content_score, media_score, review_score, digital_asset_score
    )

    print(f"Brand: {result['brand']}")
    print(f"Audit Type: {result['audit_type']}")
    print("=" * 45)
    print(f"Search Visibility Score:       {result['search_visibility_score']}/100  [{get_status(result['search_visibility_score'])}]")
    print(f"Mention Score:                 {result['mention_score']}/100  [{get_status(result['mention_score'])}]")
    print(f"Content Score:                 {result['content_score']}/100  [{get_status(result['content_score'])}]")
    print(f"Media Score:                   {result['media_score']}/100  [{get_status(result['media_score'])}]")
    print(f"Review Score:                  {result['review_score']}/100  [{get_status(result['review_score'])}]")
    print(f"Digital Asset Score:           {result['digital_asset_score']}/100  [{get_status(result['digital_asset_score'])}]")
    print("=" * 45)
    print(f"Overall Reputation Index:      {result['overall_reputation_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nReputation Channels:")
    for channel, score in result['reputation_channels'].items():
        print(f"  {channel:<24} {score}/100")


if __name__ == "__main__":
    main()
