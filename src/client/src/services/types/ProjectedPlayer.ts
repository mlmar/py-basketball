import type { BasePlayer } from "@/services/types/BasePlayer"

export interface ProjectedPlayer {
    num_games: number;
    opponents: string[];
    game_dates: string[];
    analysis: string;
    player: BasePlayer,
    tags: string[];
    rank: number;
    prev_rank: number;
}