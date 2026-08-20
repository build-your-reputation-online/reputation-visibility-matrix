#!/usr/bin/env node

interface ReputationMatrixInput {
  brand: string;
  auditType: string;
  searchVisibility: number;
  mentionScore: number;
  contentScore: number;
  mediaScore: number;
  reviewScore: number;
  digitalAssetScore: number;
}

interface ReputationMatrixOutput {
  brand: string;
  auditType: string;
  searchVisibilityScore: number;
  mentionScore: number;
  contentScore: number;
  mediaScore: number;
  reviewScore: number;
  digitalAssetScore: number;
  overallReputationIndex: number;
  priorityAction: string;
  reputationChannels: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function formatAuditType(auditType: string): string {
  return auditType.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ");
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    searchVisibility: "Search Visibility",
    mention: "Mention",
    content: "Content",
    media: "Media",
    review: "Review",
    digitalAsset: "Digital Asset",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getReputationChannels(search: number, mention: number, review: number, media: number): Record<string, number> {
  return {
    "Branded Search": Math.min(100, Math.round(search * 1.0)),
    "Social Mentions": Math.min(100, Math.round(mention * 1.0)),
    "Review Platforms": Math.min(100, Math.round(review * 1.0)),
    "Media Coverage": Math.min(100, Math.round(media * 1.0)),
  };
}

export function runReputationMatrix(input: ReputationMatrixInput): ReputationMatrixOutput {
  const scores = {
    searchVisibility: input.searchVisibility,
    mention: input.mentionScore,
    content: input.contentScore,
    media: input.mediaScore,
    review: input.reviewScore,
    digitalAsset: input.digitalAssetScore,
  };
  const overallReputationIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    brand: input.brand,
    auditType: formatAuditType(input.auditType),
    searchVisibilityScore: input.searchVisibility,
    mentionScore: input.mentionScore,
    contentScore: input.contentScore,
    mediaScore: input.mediaScore,
    reviewScore: input.reviewScore,
    digitalAssetScore: input.digitalAssetScore,
    overallReputationIndex,
    priorityAction: getPriorityAction(scores),
    reputationChannels: getReputationChannels(input.searchVisibility, input.mentionScore, input.reviewScore, input.mediaScore),
  };
}

const args = process.argv.slice(2);
const brand = args[0] || "brand-name";
const auditType = args[1] || "full-audit";
const searchVisibility = parseInt(args[2]) || 88;
const mentionScore = parseInt(args[3]) || 82;
const contentScore = parseInt(args[4]) || 85;
const mediaScore = parseInt(args[5]) || 78;
const reviewScore = parseInt(args[6]) || 90;
const digitalAssetScore = parseInt(args[7]) || 84;

const result = runReputationMatrix({
  brand, auditType, searchVisibility, mentionScore,
  contentScore, mediaScore, reviewScore, digitalAssetScore,
});

console.log(`Brand: ${result.brand}`);
console.log(`Audit Type: ${result.auditType}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Search Visibility Score:       ${result.searchVisibilityScore}/100  [${getStatus(result.searchVisibilityScore)}]`);
console.log(`Mention Score:                 ${result.mentionScore}/100  [${getStatus(result.mentionScore)}]`);
console.log(`Content Score:                 ${result.contentScore}/100  [${getStatus(result.contentScore)}]`);
console.log(`Media Score:                   ${result.mediaScore}/100  [${getStatus(result.mediaScore)}]`);
console.log(`Review Score:                  ${result.reviewScore}/100  [${getStatus(result.reviewScore)}]`);
console.log(`Digital Asset Score:           ${result.digitalAssetScore}/100  [${getStatus(result.digitalAssetScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Reputation Index:      ${result.overallReputationIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nReputation Channels:");
Object.entries(result.reputationChannels).forEach(([channel, score]) => {
  console.log(`  ${channel.padEnd(22)} ${score}/100`);
});
