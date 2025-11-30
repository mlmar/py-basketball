import type { BasePlayer } from "@/services/types/BasePlayer";

export interface Player extends BasePlayer {
    mp: string;
    fg: number;
    fga: number;
    fg_pct: number;
    fg3: number;
    fg3a: number;
    fg3_pct: number;
    ft: number;
    fta: number;
    ft_pct: number;
    orb: number;
    drb: number;
    trb: number;
    ast: number;
    stl: number;
    blk: number;
    tov: number;
    pts: number;
    plus_minus: number;
    date: number;
}