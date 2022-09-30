_base_ = [
    '../_base_/models/swin_transformer_v2/base_256.py',
    '../_base_/datasets/imagenet_bs64_swin_256.py',
    '../_base_/schedules/imagenet_bs1024_adamw_swin.py',
    '../_base_/default_runtime.py'
]

model = dict(
    type='ImageClassifier',
    backbone=dict(
        window_size=[16, 16, 16, 8],
        drop_path_rate=0.2,
        pretrained_window_sizes=[12, 12, 12, 6]))
