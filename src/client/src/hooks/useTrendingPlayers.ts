import { StatsService } from "@/services/StatsService";
import { useQuery } from "@tanstack/react-query";

type UseStatsAnalysisResult = {
    data: Awaited<ReturnType<typeof StatsService.getTrendingAnalysis>> | undefined,
    isLoading: boolean,
    isError: boolean
}

/**
 * Retrieves most recent trending player analysis 
 * @returns 
 */
export function useTrendingplayers(limit: number = 20): UseStatsAnalysisResult {
    const { data, isLoading, isError } = useQuery({
        queryKey: ['stats-analysis', limit],
        queryFn: async () => await StatsService.getTrendingAnalysis(),
        staleTime: Infinity,
        placeholderData: (previousData) => previousData,
        refetchOnMount: false,
        select: (data) => {
            return data.slice(0, limit)
        }
    });

    return { data, isLoading, isError }
}