import { StatsService } from "@/services/StatsService";
import type { TrendingPlayer } from "@/services/types/TrendingPlayer";
import { useQuery } from "@tanstack/react-query";

type UseTrendingPlayersResult = {
    data: Awaited<ReturnType<typeof StatsService.getTrendingAnalysis>>,
    isLoading: boolean,
    isError: boolean
}

/**
 * Retrieves most recent trending player analysis 
 * @param {string | null} trendingFilter -- tag to filter by
 * @param {number} limit -- limit number of returned players
 * @return {UseTrendingPlayersResult}
 */
export function useTrendingplayers(trendingFilter: string | null, limit: number = 20): UseTrendingPlayersResult {
    const { data = { result: [], status: 'PROCESSING', is_all_records: true }, isLoading, isError } = useQuery({
        queryKey: ['trending-analysis', limit],
        queryFn: async () => await StatsService.getTrendingAnalysis(limit),
        select: (data) => {
            return {
                ...data,
                result: data.result?.filter((player: TrendingPlayer) => {
                    if (trendingFilter) {
                        return player.tags.includes(trendingFilter)
                    }
                    return true;
                })
            }
        }
    });

    return { data, isLoading, isError }
}