import { StatsService } from "@/services/StatsService";
import { useQuery } from "@tanstack/react-query";

/**
 * Retrieves player averages from the last N days
 * @param {number} days 
 * @returns 
 */
export function useStatsAverages(days: number) {
    const { data, isLoading, isError } = useQuery({
        queryKey: ['stats-averages', days],
        queryFn: async () => await StatsService.getAverages(days),
        staleTime: Infinity,
        placeholderData: (previousData) => previousData
    });

    return { data, isLoading, isError }
}