import { useQuery } from "@tanstack/react-query";
import { StatsService } from "@/services/StatsService";

type UseProjectedAnalysisResult = {
    data: Awaited<ReturnType<typeof StatsService.getProjectedAnalysis>>,
    isLoading: boolean,
    isError: boolean
}

/**
 * Retrieves most recent player analysis 
 * @returns 
 */
export function useProjectedAnalysis(): UseProjectedAnalysisResult {
    const { data = { result: [], status: null }, isLoading, isError } = useQuery({
        queryKey: ['stats-analysis'],
        queryFn: async () => await StatsService.getProjectedAnalysis(),
    });

    return { data, isLoading, isError }
}