import { StatsService } from "@/services/StatsService";
import { useQuery } from "@tanstack/react-query";

type UseStatsAnalysisResult = {
    data: Awaited<ReturnType<typeof StatsService.getAnalysis>> | undefined,
    isLoading: boolean,
    isError: boolean
}

/**
 * Retrieves most recent player analysis 
 * @returns 
 */
export function useStatsAnalysis(): UseStatsAnalysisResult {
    const { data, isLoading, isError } = useQuery({
        queryKey: ['stats-analysis'],
        queryFn: async () => await StatsService.getAnalysis(),
        staleTime: Infinity,
        placeholderData: (previousData) => previousData,
        refetchOnMount: false
    });

    return { data, isLoading, isError }
}