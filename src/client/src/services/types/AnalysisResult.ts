export interface AnalysisResult<T> {
    result: T[],
    status: string | null | undefined
}