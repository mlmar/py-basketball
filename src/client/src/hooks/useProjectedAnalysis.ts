import { StatsService } from "@/services/StatsService";
import { useQuery } from "@tanstack/react-query";

type UseProjectedAnalysisResult = {
    data: Awaited<ReturnType<typeof StatsService.getProjectedAnalysis>> | undefined,
    isLoading: boolean,
    isError: boolean
}

/**
 * Retrieves most recent player analysis 
 * @returns 
 */
export function useProjectedAnalysis(): UseProjectedAnalysisResult {
    const { data = [], isLoading, isError } = useQuery({
        queryKey: ['stats-analysis'],
        queryFn: async () => await StatsService.getProjectedAnalysis(),
        staleTime: Infinity,
        placeholderData: (previousData) => previousData,
        refetchOnMount: false
    });

    return { data, isLoading, isError }
}