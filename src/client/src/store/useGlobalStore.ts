import { createStoreInstance } from '@/store/createStoreInstance';

export type GlobalStore = {
    trendingFilter: string | null,
    setTrendingFilter: (prop: string | null) => void
}

export const [GlobalStoreProvider, useGlobalStore] = createStoreInstance<GlobalStore>((set) => {
    return {
        trendingFilter: '',
        setTrendingFilter: (trendingFilter: string | null = null) => {
            set({ trendingFilter });
        }
    }
})