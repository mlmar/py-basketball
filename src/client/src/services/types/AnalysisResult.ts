export interface AnalysisResult<T> {
    result: T[],
    status: string | null | undefined,
    is_all_records: boolean
}