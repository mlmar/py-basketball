import { useGlobalStore } from "@/store/useGlobalStore";

export function useIsLoggedIn(): boolean {
    return useGlobalStore(state => state.isLoggedIn);
}