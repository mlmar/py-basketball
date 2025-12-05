import { useGlobalStore, type GlobalStore } from "@/store/useGlobalStore";

type UseTrendingFilterResult = [
    trendingFilter: GlobalStore['trendingFilter'],
    setTrendingFilter: GlobalStore['setTrendingFilter'],
]

/**
 * Hook for reading and setting trending filter state
 */
export function useTrendingFilter(): UseTrendingFilterResult {
    const trendingFilter = useGlobalStore(state => state.trendingFilter);
    const setTrendingFilter = useGlobalStore(state => state.setTrendingFilter);
    return [trendingFilter, setTrendingFilter];
}