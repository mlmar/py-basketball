export interface ProjectedPlayer {
    num_games: number
    opponents: string[]
    game_dates: string[]
    analysis: string
    player: {
        id: string;
        player: string;
        team_id: string;
        opp_id: string;
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
}