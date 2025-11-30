import type { Player } from "@/services/types/Player"

export interface ProjectedPlayer {
    num_games: number
    opponents: string[]
    game_dates: string[]
    analysis: string
    player: Player
}