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
 * @return {TrendingPlayer[]}
 */
export function useTrendingplayers(trendingFilter: string | null, limit: number = 20): UseTrendingPlayersResult {
    const { data = [], isLoading, isError } = useQuery({
        queryKey: ['stats-analysis', limit],
        queryFn: async () => await StatsService.getTrendingAnalysis(),
        staleTime: Infinity,
        placeholderData: (previousData) => previousData,
        refetchOnMount: false,
        select: (data) => {
            return data.filter((player: TrendingPlayer) => {
                if (trendingFilter) {
                    return player.tags.includes(trendingFilter)
                }
                return true;
            }).slice(0, limit)
        }
    });

    return { data, isLoading, isError }
}