import type { BasePlayer } from "@/services/types/BasePlayer"

export interface TrendingPlayer {
    num_games: number
    opponents: string[]
    game_dates: string[]
    analysis: string
    player: BasePlayer,
    tags: string[]
}