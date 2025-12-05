import { createStoreInstance } from '@/store/createStoreInstance';

export type GlobalStore = {
    isLoggedIn: boolean,
    trendingFilter: string | null,
    setTrendingFilter: (prop: string | null) => void
}

export const [GlobalStoreProvider, useGlobalStore] = createStoreInstance<GlobalStore>((set) => {
    return {
        isLoggedIn: false,
        trendingFilter: null,
        setTrendingFilter: (trendingFilter: string | null = null) => {
            set({ trendingFilter });
        }
    }
})