import { create } from 'zustand';

type GlobalStore = {
    example: string | null;
    setExample: (prop: string) => void;
};

export const useGlobalStore = create<GlobalStore>((set) => {
    return {
        example: null,
        setExample: (prop: string) => {
            set({ example: prop });
        }
    };
});
