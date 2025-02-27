from .evaluator_vcoco import vcoco_evaluate, vcoco_accumulate

def hoi_evaluator(args, model, criterion, postprocessors, data_loader, device, thr=0):
    if args.dataset_file == 'vcoco':
        return vcoco_evaluate(model, criterion, postprocessors, data_loader, device, args.output_dir, thr)
    else: raise NotImplementedError

def hoi_accumulator(args, total_res, print_results=False, wandb=False):
    if args.dataset_file == 'vcoco':
        return vcoco_accumulate(total_res, args, print_results, wandb)
    else: raise NotImplementedError