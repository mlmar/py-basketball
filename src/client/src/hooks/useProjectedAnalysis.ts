import { useQuery } from "@tanstack/react-query";
import { StatsService } from "@/services/StatsService";

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
        queryFn: async () => await StatsService.getProjectedAnalysis()
    });

    return { data, isLoading, isError }
}