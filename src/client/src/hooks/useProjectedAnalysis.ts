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
export function useProjectedAnalysis(limit: number = 20): UseProjectedAnalysisResult {
    const { data = { result: [], status: null, is_all_records: true }, isLoading, isError } = useQuery({
        queryKey: ['stats-analysis'],
        queryFn: async () => await StatsService.getProjectedAnalysis(limit),
    });

    return { data, isLoading, isError }
}