import { createFileRoute } from '@tanstack/react-router';
import { WaiverBoard } from '@/features/WaiverBoard';

export const Route = createFileRoute('/waiver')({
    component: WaiverBoard
});
