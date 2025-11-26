import { createStoreInstance } from '@/store/createStoreInstance';

type GlobalStore = {
    example: string,
    setExample: (prop: string) => void
}

export const [GlobalStoreProvider, useGlobalStore] = createStoreInstance<GlobalStore>((set) => {
    return {
        example: '',
        setExample: (prop) => {
            set({ example: prop });
        }
    }
})