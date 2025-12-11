import { StatsService } from "@/services/StatsService";
import type { TrendingPlayer } from "@/services/types/TrendingPlayer";
import { useQuery } from "@tanstack/react-query";

type UseTrendingPlayersResult = {
    data: Awaited<ReturnType<typeof StatsService.getTrendingAnalysis>>,
    isLoading: boolean,
    isError: boolean,
    isAllData: boolean
}

/**
 * Retrieves most recent trending player analysis 
 * @param {string | null} trendingFilter -- tag to filter by
 * @param {number} limit -- limit number of returned players
 * @return {UseTrendingPlayersResult}
 */
export function useTrendingplayers(trendingFilter: string | null, limit: number = 20): UseTrendingPlayersResult {
    const { data, isLoading, isError, } = useQuery({
        queryKey: ['stats-analysis', limit],
        queryFn: async () => await StatsService.getTrendingAnalysis()
    });

    const filteredResult = data?.result?.filter((player: TrendingPlayer) => {
        if (trendingFilter) {
            return player.tags.includes(trendingFilter)
        }
        return true;
    });

    const limitedResult = filteredResult?.slice(0, limit) ?? [];

    const finalData = {
        ...data,
        status: data?.status,
        result: limitedResult ?? []
    }

    return { data: finalData, isLoading, isError, isAllData: filteredResult?.length === limitedResult?.length }
}